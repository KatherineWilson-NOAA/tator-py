# tator
Interface to the Tator backend.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 0.0.2
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import tator
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tator
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import tator
from tator.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tator.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration = tator.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'


# Enter a context with an instance of the API client
with tator.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tator.TatorApi(api_client)
    project = 56 # int | A unique integer identifying a project.
algorithm_launch_spec = {"algorithm_name":"My Algorithm","media_ids":[1,5,10]} # AlgorithmLaunchSpec |  (optional)

    try:
        api_response = api_instance.algorithm_launch(project, algorithm_launch_spec=algorithm_launch_spec)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TatorApi->algorithm_launch: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TatorApi* | [**algorithm_launch**](docs/TatorApi.md#algorithm_launch) | **POST** /rest/AlgorithmLaunch/{project} | 
*TatorApi* | [**create_analysis**](docs/TatorApi.md#create_analysis) | **POST** /rest/Analyses/{project} | 
*TatorApi* | [**create_leaf**](docs/TatorApi.md#create_leaf) | **POST** /rest/Leaves/{project} | 
*TatorApi* | [**create_leaf_type**](docs/TatorApi.md#create_leaf_type) | **POST** /rest/LeafTypes/{project} | 
*TatorApi* | [**create_localization**](docs/TatorApi.md#create_localization) | **POST** /rest/Localizations/{project} | 
*TatorApi* | [**create_localization_type**](docs/TatorApi.md#create_localization_type) | **POST** /rest/LocalizationTypes/{project} | 
*TatorApi* | [**create_media_type**](docs/TatorApi.md#create_media_type) | **POST** /rest/MediaTypes/{project} | 
*TatorApi* | [**create_membership**](docs/TatorApi.md#create_membership) | **POST** /rest/Memberships/{project} | 
*TatorApi* | [**create_obtain_auth_token**](docs/TatorApi.md#create_obtain_auth_token) | **POST** /rest/Token | 
*TatorApi* | [**create_progress_summary_api**](docs/TatorApi.md#create_progress_summary_api) | **POST** /rest/ProgressSummary/{project} | 
*TatorApi* | [**create_project**](docs/TatorApi.md#create_project) | **POST** /rest/Projects | 
*TatorApi* | [**create_state**](docs/TatorApi.md#create_state) | **POST** /rest/States/{project} | 
*TatorApi* | [**create_state_type**](docs/TatorApi.md#create_state_type) | **POST** /rest/StateTypes/{project} | 
*TatorApi* | [**create_temporary_file**](docs/TatorApi.md#create_temporary_file) | **POST** /rest/TemporaryFiles/{project} | 
*TatorApi* | [**create_version**](docs/TatorApi.md#create_version) | **POST** /rest/Versions/{project} | 
*TatorApi* | [**delete_job**](docs/TatorApi.md#delete_job) | **DELETE** /rest/Job/{run_uid} | 
*TatorApi* | [**delete_job_group**](docs/TatorApi.md#delete_job_group) | **DELETE** /rest/JobGroup/{group_id} | 
*TatorApi* | [**delete_leaf**](docs/TatorApi.md#delete_leaf) | **DELETE** /rest/Leaf/{id} | 
*TatorApi* | [**delete_leaf_list**](docs/TatorApi.md#delete_leaf_list) | **DELETE** /rest/Leaves/{project} | 
*TatorApi* | [**delete_leaf_type**](docs/TatorApi.md#delete_leaf_type) | **DELETE** /rest/LeafType/{id} | 
*TatorApi* | [**delete_localization**](docs/TatorApi.md#delete_localization) | **DELETE** /rest/Localization/{id} | 
*TatorApi* | [**delete_localization_list**](docs/TatorApi.md#delete_localization_list) | **DELETE** /rest/Localizations/{project} | 
*TatorApi* | [**delete_localization_type**](docs/TatorApi.md#delete_localization_type) | **DELETE** /rest/LocalizationType/{id} | 
*TatorApi* | [**delete_media**](docs/TatorApi.md#delete_media) | **DELETE** /rest/Media/{id} | 
*TatorApi* | [**delete_media_list**](docs/TatorApi.md#delete_media_list) | **DELETE** /rest/Medias/{project} | 
*TatorApi* | [**delete_media_type**](docs/TatorApi.md#delete_media_type) | **DELETE** /rest/MediaType/{id} | 
*TatorApi* | [**delete_membership**](docs/TatorApi.md#delete_membership) | **DELETE** /rest/Membership/{id} | 
*TatorApi* | [**delete_project**](docs/TatorApi.md#delete_project) | **DELETE** /rest/Project/{id} | 
*TatorApi* | [**delete_state**](docs/TatorApi.md#delete_state) | **DELETE** /rest/State/{id} | 
*TatorApi* | [**delete_state_list**](docs/TatorApi.md#delete_state_list) | **DELETE** /rest/States/{project} | 
*TatorApi* | [**delete_state_type**](docs/TatorApi.md#delete_state_type) | **DELETE** /rest/StateType/{id} | 
*TatorApi* | [**delete_temporary_file**](docs/TatorApi.md#delete_temporary_file) | **DELETE** /rest/TemporaryFile/{id} | 
*TatorApi* | [**delete_temporary_file_list**](docs/TatorApi.md#delete_temporary_file_list) | **DELETE** /rest/TemporaryFiles/{project} | 
*TatorApi* | [**delete_version**](docs/TatorApi.md#delete_version) | **DELETE** /rest/Version/{id} | 
*TatorApi* | [**get_algorithm_list**](docs/TatorApi.md#get_algorithm_list) | **GET** /rest/Algorithms/{project} | 
*TatorApi* | [**get_analysis_list**](docs/TatorApi.md#get_analysis_list) | **GET** /rest/Analyses/{project} | 
*TatorApi* | [**get_clip**](docs/TatorApi.md#get_clip) | **GET** /rest/GetClip/{id} | 
*TatorApi* | [**get_frame**](docs/TatorApi.md#get_frame) | **GET** /rest/GetFrame/{id} | 
*TatorApi* | [**get_leaf**](docs/TatorApi.md#get_leaf) | **GET** /rest/Leaf/{id} | 
*TatorApi* | [**get_leaf_list**](docs/TatorApi.md#get_leaf_list) | **GET** /rest/Leaves/{project} | 
*TatorApi* | [**get_leaf_type**](docs/TatorApi.md#get_leaf_type) | **GET** /rest/LeafType/{id} | 
*TatorApi* | [**get_leaf_type_list**](docs/TatorApi.md#get_leaf_type_list) | **GET** /rest/LeafTypes/{project} | 
*TatorApi* | [**get_localization**](docs/TatorApi.md#get_localization) | **GET** /rest/Localization/{id} | 
*TatorApi* | [**get_localization_list**](docs/TatorApi.md#get_localization_list) | **GET** /rest/Localizations/{project} | 
*TatorApi* | [**get_localization_type**](docs/TatorApi.md#get_localization_type) | **GET** /rest/LocalizationType/{id} | 
*TatorApi* | [**get_localization_type_list**](docs/TatorApi.md#get_localization_type_list) | **GET** /rest/LocalizationTypes/{project} | 
*TatorApi* | [**get_media**](docs/TatorApi.md#get_media) | **GET** /rest/Media/{id} | 
*TatorApi* | [**get_media_list**](docs/TatorApi.md#get_media_list) | **GET** /rest/Medias/{project} | 
*TatorApi* | [**get_media_next**](docs/TatorApi.md#get_media_next) | **GET** /rest/MediaNext/{id} | 
*TatorApi* | [**get_media_prev**](docs/TatorApi.md#get_media_prev) | **GET** /rest/MediaPrev/{id} | 
*TatorApi* | [**get_media_sections**](docs/TatorApi.md#get_media_sections) | **GET** /rest/MediaSections/{project} | 
*TatorApi* | [**get_media_type**](docs/TatorApi.md#get_media_type) | **GET** /rest/MediaType/{id} | 
*TatorApi* | [**get_media_type_list**](docs/TatorApi.md#get_media_type_list) | **GET** /rest/MediaTypes/{project} | 
*TatorApi* | [**get_membership**](docs/TatorApi.md#get_membership) | **GET** /rest/Membership/{id} | 
*TatorApi* | [**get_membership_list**](docs/TatorApi.md#get_membership_list) | **GET** /rest/Memberships/{project} | 
*TatorApi* | [**get_project**](docs/TatorApi.md#get_project) | **GET** /rest/Project/{id} | 
*TatorApi* | [**get_project_list**](docs/TatorApi.md#get_project_list) | **GET** /rest/Projects | 
*TatorApi* | [**get_section_analysis**](docs/TatorApi.md#get_section_analysis) | **GET** /rest/SectionAnalysis/{project} | 
*TatorApi* | [**get_state**](docs/TatorApi.md#get_state) | **GET** /rest/State/{id} | 
*TatorApi* | [**get_state_graphic**](docs/TatorApi.md#get_state_graphic) | **GET** /rest/StateGraphic/{id} | 
*TatorApi* | [**get_state_list**](docs/TatorApi.md#get_state_list) | **GET** /rest/States/{project} | 
*TatorApi* | [**get_state_type**](docs/TatorApi.md#get_state_type) | **GET** /rest/StateType/{id} | 
*TatorApi* | [**get_state_type_list**](docs/TatorApi.md#get_state_type_list) | **GET** /rest/StateTypes/{project} | 
*TatorApi* | [**get_temporary_file**](docs/TatorApi.md#get_temporary_file) | **GET** /rest/TemporaryFile/{id} | 
*TatorApi* | [**get_temporary_file_list**](docs/TatorApi.md#get_temporary_file_list) | **GET** /rest/TemporaryFiles/{project} | 
*TatorApi* | [**get_user**](docs/TatorApi.md#get_user) | **GET** /rest/User/{id} | 
*TatorApi* | [**get_version**](docs/TatorApi.md#get_version) | **GET** /rest/Version/{id} | 
*TatorApi* | [**get_version_list**](docs/TatorApi.md#get_version_list) | **GET** /rest/Versions/{project} | 
*TatorApi* | [**leaf_suggestion**](docs/TatorApi.md#leaf_suggestion) | **GET** /rest/Leaves/Suggestion/{ancestor}/{project} | 
*TatorApi* | [**notify**](docs/TatorApi.md#notify) | **POST** /rest/Notify | 
*TatorApi* | [**progress**](docs/TatorApi.md#progress) | **POST** /rest/Progress/{project} | 
*TatorApi* | [**save_image**](docs/TatorApi.md#save_image) | **POST** /rest/SaveImage/{project} | 
*TatorApi* | [**save_video**](docs/TatorApi.md#save_video) | **POST** /rest/SaveVideo/{project} | 
*TatorApi* | [**transcode**](docs/TatorApi.md#transcode) | **POST** /rest/Transcode/{project} | 
*TatorApi* | [**update_leaf**](docs/TatorApi.md#update_leaf) | **PATCH** /rest/Leaf/{id} | 
*TatorApi* | [**update_leaf_list**](docs/TatorApi.md#update_leaf_list) | **PATCH** /rest/Leaves/{project} | 
*TatorApi* | [**update_leaf_type**](docs/TatorApi.md#update_leaf_type) | **PATCH** /rest/LeafType/{id} | 
*TatorApi* | [**update_localization**](docs/TatorApi.md#update_localization) | **PATCH** /rest/Localization/{id} | 
*TatorApi* | [**update_localization_list**](docs/TatorApi.md#update_localization_list) | **PATCH** /rest/Localizations/{project} | 
*TatorApi* | [**update_localization_type**](docs/TatorApi.md#update_localization_type) | **PATCH** /rest/LocalizationType/{id} | 
*TatorApi* | [**update_media**](docs/TatorApi.md#update_media) | **PATCH** /rest/Media/{id} | 
*TatorApi* | [**update_media_list**](docs/TatorApi.md#update_media_list) | **PATCH** /rest/Medias/{project} | 
*TatorApi* | [**update_media_type**](docs/TatorApi.md#update_media_type) | **PATCH** /rest/MediaType/{id} | 
*TatorApi* | [**update_membership**](docs/TatorApi.md#update_membership) | **PATCH** /rest/Membership/{id} | 
*TatorApi* | [**update_project**](docs/TatorApi.md#update_project) | **PATCH** /rest/Project/{id} | 
*TatorApi* | [**update_state**](docs/TatorApi.md#update_state) | **PATCH** /rest/State/{id} | 
*TatorApi* | [**update_state_list**](docs/TatorApi.md#update_state_list) | **PATCH** /rest/States/{project} | 
*TatorApi* | [**update_state_type**](docs/TatorApi.md#update_state_type) | **PATCH** /rest/StateType/{id} | 
*TatorApi* | [**update_user**](docs/TatorApi.md#update_user) | **PATCH** /rest/User/{id} | 
*TatorApi* | [**update_version**](docs/TatorApi.md#update_version) | **PATCH** /rest/Version/{id} | 
*TatorApi* | [**update_video**](docs/TatorApi.md#update_video) | **PATCH** /rest/SaveVideo/{project} | 
*TatorApi* | [**whoami**](docs/TatorApi.md#whoami) | **GET** /rest/User/GetCurrent | 


## Documentation For Models

 - [Algorithm](docs/Algorithm.md)
 - [AlgorithmLaunch](docs/AlgorithmLaunch.md)
 - [AlgorithmLaunchSpec](docs/AlgorithmLaunchSpec.md)
 - [Analysis](docs/Analysis.md)
 - [AnalysisSpec](docs/AnalysisSpec.md)
 - [AttributeBulkUpdate](docs/AttributeBulkUpdate.md)
 - [AttributeType](docs/AttributeType.md)
 - [AttributeTypeUpdate](docs/AttributeTypeUpdate.md)
 - [AutocompleteService](docs/AutocompleteService.md)
 - [BadRequestResponse](docs/BadRequestResponse.md)
 - [Color](docs/Color.md)
 - [ColorMap](docs/ColorMap.md)
 - [CreateResponse](docs/CreateResponse.md)
 - [Credentials](docs/Credentials.md)
 - [ImageSpec](docs/ImageSpec.md)
 - [Leaf](docs/Leaf.md)
 - [LeafSpec](docs/LeafSpec.md)
 - [LeafSuggestion](docs/LeafSuggestion.md)
 - [LeafType](docs/LeafType.md)
 - [LeafTypeSpec](docs/LeafTypeSpec.md)
 - [LeafTypeUpdate](docs/LeafTypeUpdate.md)
 - [LeafUpdate](docs/LeafUpdate.md)
 - [Localization](docs/Localization.md)
 - [LocalizationSpec](docs/LocalizationSpec.md)
 - [LocalizationType](docs/LocalizationType.md)
 - [LocalizationTypeSpec](docs/LocalizationTypeSpec.md)
 - [LocalizationTypeUpdate](docs/LocalizationTypeUpdate.md)
 - [LocalizationUpdate](docs/LocalizationUpdate.md)
 - [Media](docs/Media.md)
 - [MediaNext](docs/MediaNext.md)
 - [MediaPrev](docs/MediaPrev.md)
 - [MediaType](docs/MediaType.md)
 - [MediaTypeSpec](docs/MediaTypeSpec.md)
 - [MediaTypeUpdate](docs/MediaTypeUpdate.md)
 - [MediaUpdate](docs/MediaUpdate.md)
 - [Membership](docs/Membership.md)
 - [MembershipSpec](docs/MembershipSpec.md)
 - [MembershipUpdate](docs/MembershipUpdate.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [NotFoundResponse](docs/NotFoundResponse.md)
 - [NotifySpec](docs/NotifySpec.md)
 - [ProgressSpec](docs/ProgressSpec.md)
 - [ProgressSummarySpec](docs/ProgressSummarySpec.md)
 - [Project](docs/Project.md)
 - [ProjectSpec](docs/ProjectSpec.md)
 - [State](docs/State.md)
 - [StateSpec](docs/StateSpec.md)
 - [StateType](docs/StateType.md)
 - [StateTypeSpec](docs/StateTypeSpec.md)
 - [StateTypeUpdate](docs/StateTypeUpdate.md)
 - [StateUpdate](docs/StateUpdate.md)
 - [TemporaryFile](docs/TemporaryFile.md)
 - [TemporaryFileSpec](docs/TemporaryFileSpec.md)
 - [Token](docs/Token.md)
 - [Transcode](docs/Transcode.md)
 - [TranscodeSpec](docs/TranscodeSpec.md)
 - [User](docs/User.md)
 - [UserUpdate](docs/UserUpdate.md)
 - [Version](docs/Version.md)
 - [VersionSpec](docs/VersionSpec.md)
 - [VersionUpdate](docs/VersionUpdate.md)
 - [VideoSpec](docs/VideoSpec.md)
 - [VideoUpdate](docs/VideoUpdate.md)


## Documentation For Authorization


## TokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




