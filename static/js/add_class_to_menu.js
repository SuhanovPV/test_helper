function addClass() {
  const href = document.location.pathname;
  const current = document.querySelector(`a[href='${href}']`);
  current.className = 'current';
}

addClass();