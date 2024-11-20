import { get, post } from '@/utils/axios.js'

export const summary = (params) => get('summary', params)
export const detailPrefix = (params) => get('detail/prefix', params)

// TODO: You need to implement more API functions for further development