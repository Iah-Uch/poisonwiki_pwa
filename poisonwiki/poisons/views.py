from typing import Any
from django.http import HttpRequest, HttpResponseNotFound, HttpResponse
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.views.generic.edit import FormView
from .models import Poison
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import datetime
from django_filters.views import FilterView
from django.urls import reverse
from urllib.parse import urlencode
from django_filters.views import FilterView
from .filters import PoisonFilter


# class PoisonCreateView(CreateView):
#     model = Poison
#     form_class = PoisonForm
#     template_name = "components/htmx_messages.html"  # Define your own template for the modal form

#     def get_success_url(self):
#         return reverse_lazy("Poisons:list")  # Redirect after successful form submission

#     def form_invalid(self, form):
#         """
#         Handle invalid form submission: display errors via messages and return a 400 status code.
#         """
#         for field, errors in form.errors.items():
#             for error in errors:
#                 messages.error(self.request, error)
#         response = super().form_invalid(form)
#         response.status_code = 400
#         return response

#     def get_form_kwargs(self):
#         """
#         Add the request to the form kwargs so it can be used in the form class if needed.
#         """
#         kwargs = super().get_form_kwargs()
#         kwargs.update({"initial": {"request": self.request}})
#         return kwargs

#     def post(self, request: HttpRequest, *args: Any, **kwargs: Any):
#         transcription = request.POST.get("transcription")

#         # Handle the first POST request (transcription sent, form dynamically generated)
#         if transcription:
#             # Dynamically generate the form based on the transcription
#             form = self.form_class(transcription=transcription)
#             # Render the form in a modal for the user to input quantities and weights
#             if form.fields:
#                 return render(request, "partials/Poison_form.html", {"form": form})

#             return HttpResponse("No matches found in the TACO database.", status=400)

#         # Handle the final POST request (form submission)
#         else:
#             return super().post(request, *args, **kwargs)


class PoisonListView(FilterView):
    model = Poison
    template_name = "pages/home.html"
    context_object_name = "poisons"
    queryset = Poison.objects.all()
    ordering = "-created_at"
    paginate_by = 10
    filterset_class = PoisonFilter
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(created_at__date=datetime.today()).order_by(
    #         self.ordering
    #     )

    def get_template_names(self):
        if self.request.htmx:
            return "partials/poison_list.html"
        return super(PoisonListView, self).get_template_names()

    def get_context_data(self, **kwargs):
        context = super(PoisonListView, self).get_context_data(**kwargs)
        # if not self.request.htmx:
        context["title"] = "Home"
        context["today"] = datetime.today().date()
        context["bottom_nav_enabled"] = False
        # Pagination URL modification for HTMX infinite scroll
        page_param = self.request.GET.copy()
        if context["page_obj"].has_next():
            page_param["page"] = context["page_obj"].next_page_number()

        query_param_list = [(key, value) for key, value in page_param.lists()]
        context["pagination_url"] = (
            f"{reverse('poisons:list')}?{urlencode(query_param_list, doseq=True)}"
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs


class PoisonDetailView(DetailView):
    model = Poison
    template_name = "partials/poison_detail.html"
    context_object_name = "poison"
    queryset = Poison.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PoisonDetailView, self).get_context_data(**kwargs)
        context["title"] = "Poison Detail"
        return context


# class PoisonHistoryListView(LoginRequiredMixin, FilterView):
#     model = Poison
#     template_name = "pages/history.html"
#     context_object_name = "Poisons"
#     queryset = Poison.objects.all().order_by("-created_at")
#     paginate_by = 2  # Number of days per page
#     filterset_class = PoisonFilter
#     paginator_class = DayPaginator  # Use the custom paginator

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "History"
#         context["bottom_nav_enabled"] = False

#         # Pagination URL modification for HTMX infinite scroll
#         page_param = self.request.GET.copy()
#         if context["page_obj"].has_next():
#             page_param["page"] = context["page_obj"].next_page_number()

#         query_param_list = [(key, value) for key, value in page_param.lists()]
#         context["pagination_url"] = (
#             f"{reverse('Poisons:history')}?{urlencode(query_param_list, doseq=True)}"
#         )
#         return context

#     def get_template_names(self):
#         if self.request.htmx:
#             return "partials/Poison_history_list.html"
#         return super(PoisonHistoryListView, self).get_template_names()

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
#         return self.filterset.qs


# class PoisonDetailView(LoginRequiredMixin, DetailView):
#     model = Poison
#     template_name = "partials/Poison_detail.html"
#     context_object_name = "Poison"
#     queryset = Poison.objects.all()

#     # TODO: Secure protected fields
#     # TODO: Make fallback routine
#     # TODO: Full dict operations
#     def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
#         if self.request.GET.get("field", None):
#             field_data = getattr(
#                 self.get_object(), self.request.GET.get("field", None), None
#             )
#             if field_data:
#                 return HttpResponse(field_data)
#             return HttpResponseNotFound()

#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super(PoisonDetailView, self).get_context_data(**kwargs)
#         context["title"] = "Poison Detail"
#         context["bottom_nav_enabled"] = False
#         return context


# class PoisonUpdateView(LoginRequiredMixin, UpdateView):
#     model = Poison
#     form_class = PoisonUpdateForm
#     template_name = "partials/update_Poison.html"
#     context_object_name = "Poison"
#     success_url = reverse_lazy("Poisons:history")


# class PoisonDeleteView(LoginRequiredMixin, DeleteView):
# model = Poison
# template_name = "partials/delete_poison.html"
# context_object_name = "poison"

# def get_context_data(self, **kwargs: Any):
#     context = super().get_context_data(**kwargs)
#     if self.request.htmx:
#         context["redirect_url"] = self.request.htmx.current_url
#     return context

# def get_success_url(self) -> str:
#     return self.request.POST.get("redirect_url", reverse_lazy("Poisons:list"))
