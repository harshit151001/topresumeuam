resume_shortlisting_functions = [
   {
       'name': "calculate_score",
       'description': "Calculates the score on scale of 1-100 for a resume based on the job description",
       'parameters': {
           'type': 'object',
           'properties': {
               'match_score': {
                     'type': 'integer',
                     'description': 'The score depicting likelihood of resume(candidate) getting shorlisted based on experiences, projects and skills on resume with respect to job description.'
               } 
          }
       }
   }
]

extract_information_functions = [
    {
        'name': "extract_information",
        'description': "Extracts projects, professional_experience and college for a resume",
        'parameters': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'Name of the candidate'
                },
                'projects': {
                    'type': 'array',
                    'description': 'List of projects done by the candidate',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'project_title': {
                                'type': 'string',
                                'description': 'Title of the project'
                            },
                            'short_description': {
                                'type': 'string',
                                'description': 'Short description of the project'
                            },
                            'tech_stack': {
                                'type': 'array',
                                'description': 'List of technologies used in the project',
                                'items': {
                                    'type': 'string'
                                }
                            },
                            'time_duration': {
                                'type': 'object',
                                'properties': {
                                    'start': {
                                        'type': 'string',
                                        'description': 'Start date of the project'
                                    },
                                    'end': {
                                        'type': 'string',
                                        'description': 'End date of the project'
                                    },
                                    'duration': {
                                        'type': 'string',
                                        'description': 'Duration of the project'
                                    }
                                }
                            },
                            'relevancy': {
                                'type': 'integer',
                                'description': 'Relevancy of the project with respect to the job description on scale of 1-10'
                            }
                        }
                    }
                },
                'professional_experience': {
                    'type': 'array',
                    'description': 'List of professional experiences of the candidate',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'role': {
                                'type': 'string',
                                'description': 'Role of the candidate in the organization'
                            },
                            'organization': {
                                'type': 'string',
                                'description': 'Name of the organization'
                            },
                            'short_description': {
                                'type': 'string',
                                'description': 'Short description of the work done by the candidate'
                            },
                            'tech_stack': {
                                'type': 'array',
                                'description': 'List of technologies used by the candidate',
                                'items': {
                                    'type': 'string'
                                }
                            },
                            'time_duration': {
                                'type': 'object',
                                'properties': {
                                    'start': {
                                        'type': 'string',
                                        'description': 'Start date of the project'
                                    },
                                    'end': {
                                        'type': 'string',
                                        'description': 'End date of the project'
                                    },
                                    'duration': {
                                        'type': 'string',
                                        'description': 'Duration of the project'
                                    }
                                }
                            },
                            'relevancy': {
                                'type': 'integer',
                                'description': 'Relevancy of the work done by the candidate wrt to the job description on scale of 1-10'
                            }
                        }
                    }
                },
                'college': {
                    'type': 'object',
                    'description': 'Details of college of the candidate',
                    'properties': {
                        'name': {
                            'type': 'string',
                            'description': 'Name of the college'
                        },
                        'degree': {
                            'type': 'string',
                            'description': 'Degree of the candidate'
                        },
                        'cgpa': {
                            'type': 'number',
                            'description': 'CGPA of the candidate'
                        },
                        'start': {
                            'type': 'string',
                            'description': 'Start date of the college'
                        },
                        'end': {
                            'type': 'string',
                            'description': 'End date of the college'
                        }               
                    }
                }
            }
        }
    }
]


