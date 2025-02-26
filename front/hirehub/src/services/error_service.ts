const handleError = (error: any, defaultMessage: string) => {
  let errorMessage = defaultMessage

  if (error.response.status === 500) {
    errorMessage = 'Internal server error'
    return errorMessage
  }

  // Check if running in development mode and if error response exists
  if (import.meta.env.MODE === 'development' && error?.request?.response) {
    errorMessage = error.request.response || defaultMessage
  }
  return errorMessage
}

export default handleError
