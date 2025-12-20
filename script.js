const copyButtons = document.querySelectorAll(".copy-btn");

copyButtons.forEach((button) => {
  button.addEventListener("click", async () => {
    const number = button.dataset.copy;

    if (!number) {
      return;
    }

    try {
      await navigator.clipboard.writeText(number);
      button.textContent = "Copied!";
      setTimeout(() => {
        button.textContent = "Copy number";
      }, 2000);
    } catch (error) {
      window.prompt("Copy this number:", number);
    }
  });
});
