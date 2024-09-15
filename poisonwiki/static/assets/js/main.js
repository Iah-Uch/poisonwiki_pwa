


document.addEventListener('DOMContentLoaded', function () {
  // Set Tooltips
  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));




  document.body.addEventListener('htmx:afterSettle', function (evt) {
    // Select all modal elements in the newly swapped content
    const newModals = evt.target.querySelectorAll('.modal');

    newModals.forEach(function (modal) {
      // Check if the modal should be shown (e.g., if it has a class 'show' or a data attribute)
      if (modal.classList.contains('show') || modal.getAttribute('data-show') === 'true') {
        const bootstrapModal = new bootstrap.Modal(modal);
        bootstrapModal.show();
      } else {
        // Otherwise, just create the modal
        new bootstrap.Modal(modal);
      }
    });
  });
});