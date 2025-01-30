$(document).ready(function() {
  $('#add-field').click(function() {
      const fieldHTML = `
          <div class="field-group">
              <input type="text" name="field" class="form-control" placeholder="Enter value" required>
              <button type="button" class="btn btn-danger remove-field">Delete</button>
          </div>
      `;
      $('#input-fields').append(fieldHTML);
  });

  $('.remove-field').on('click', function() {
      $(this).closest('.field-group').remove();
  });

  $('#form-with-dynamic-inputs').submit(function(e) {
      e.preventDefault();
      const formDataArray = $(this).serializeArray();
      const formData = {};
      formDataArray.forEach(item => {
          if (formData[item.name]) {
              if (Array.isArray(formData[item.name])) {
                  formData[item.name].push(item.value);
              } else {
                  formData[item.name] = [formData[item.name], item.value];
              }
          } else {
              formData[item.name] = item.value;
          }
      });

      $.ajax({
          url: '/submit',
          type: 'POST',
          contentType: 'application/json',
          data: JSON.stringify(formData),
          success: function(response) {
              alert(response.message);
              $('#form-with-dynamic-inputs')[0].reset();
              $('#input-fields').html(`
                <div class="field-group">
                  <input type="text" name="field" class="form-control" placeholder="Enter value" required>
                  <button type="button" class="btn btn-danger remove-field">Delete</button>
                </div>
              `);
          },
          error: function(xhr) {
              alert('An error occurred while saving data.');
          }
      });
  });

  $('#switch-to-show-data').click(function() {
      $.ajax({
          url: '/list',
          type: 'GET',
          success: function(response) {
              $('#form-section').hide();
              $('#data-section').show();
              $('#data-container').empty();
              if (response.data.length === 0) {
                  $('#data-container').append('<p>No data available.</p>');
              } else {
                  response.data.forEach(item => {
                      const dataHTML = `
                        <div class="data-item">
                          <strong>ID:</strong> ${item.id} <br>
                          <strong>Data:</strong>${JSON.stringify(item.data)}
                        </div>
                      `;
                      $('#data-container').append(dataHTML);
                  });
              }
          },
          error: function(xhr) {
              alert('An error occurred while fetching data.');
          }
      });
  });

  $('#back-to-form-button').click(function(){
      $('#data-section').hide();
      $('#form-section').show();
  });
});