# Project Roadmap: Pipedrive API v2 Python Client

## Introduction

This document outlines the planned development phases and priorities for the `pipedrive-v2-python` client library. Our primary goal is to provide a robust, reliable, and developer-friendly interface to the Pipedrive API v2.

## Phase 1: V2 Endpoint Testing & Validation (Highest Priority)

**Goal:** Ensure comprehensive test coverage and validate the functionality of all implemented V2 resource methods against the live Pipedrive API.

**Priorities:**
1.  **Integration Testing Framework:** Set up a testing framework (e.g., `pytest`) suitable for making live API calls in a controlled manner (using a dedicated test account/sandbox if possible).
2.  **Resource Method Tests:** Write integration tests for *every* method within each resource handler (`Activities`, `Deals`, `Persons`, `Organizations`, `Products`, `ProductVariations`, `Pipelines`, `Stages`, `DealProducts`, `Search`).
    *   Verify correct request formation (URL, method, headers, parameters, body).
    *   Validate successful response parsing for various scenarios (e.g., success with data, success with no data, pagination).
    *   Test handling of different parameter types (strings, integers, booleans, lists).
    *   Confirm expected Pydantic model validation (create/update models).
    *   Test error handling for common API errors (404 Not Found, 400/422 Validation, 401/403 Auth).
3.  **Model Refinement:** Update Pydantic models (`models/`) based on testing feedback and real-world API responses, ensuring all relevant fields and data structures are accurately represented.

## Phase 2: Helper Methods & Ergonomics

**Goal:** Enhance the library's usability by adding higher-level helper methods for common workflows and improving developer experience.

**Priorities:**
1.  **Search Helpers:** Implement methods that combine search and retrieval, e.g.,
    *   `search_person_by_email(email: str) -> Optional[dict]`
    *   `search_organization_by_name(name: str, exact_match: bool = False) -> List[dict]`
    *   `find_deal(title: str, status: str = 'open') -> Optional[dict]`
2.  **Create/Update Helpers:** Simplify common create/update patterns, e.g.,
    *   `create_or_update_person(email: str, data: dict) -> dict` (finds by email, updates if exists, creates if not)
    *   `create_or_update_deal(...)`
    *   `create_or_update_organization(...)`
3.  **Pagination Abstraction:** Explore options for simplifying pagination for the end-user (e.g., helper functions or generator methods that automatically handle `cursor`/`limit`).
4.  **Documentation & Examples:** Improve docstrings and add more comprehensive usage examples in the `README.md` based on the new helper methods.

## Phase 3: Backwards Compatibility (V1 Support - Lower Priority)

**Goal:** Explore and potentially implement support for Pipedrive API v1 endpoints where v2 alternatives are not yet available or for users needing specific v1 features.

**Considerations:**
*   **Feasibility:** Assess the complexity of maintaining compatibility with two different API versions.
*   **Implementation:**
    *   Option A: Introduce a separate `PipedriveV1Client`.
    *   Option B: Integrate V1 calls into the existing `PipedriveV2Client` with clear distinctions (e.g., `client.v1.users.list_users()`).
    *   Option C: Use conditional logic based on available endpoints (more complex).
*   **Priority:** This phase is considered lower priority than robust V2 support and usability enhancements. It will be revisited after Phases 1 and 2 are substantially complete.

## Ongoing Maintenance

*   **Bug Fixes:** Address issues reported by users or found during testing.
*   **Dependency Updates:** Keep dependencies (`requests`, `pydantic`) up-to-date.
*   **API Changes:** Monitor Pipedrive API v2 updates and adapt the library accordingly.
*   **Documentation:** Continuously improve documentation (README, docstrings, examples).

*This roadmap is subject to change based on development progress, user feedback, and Pipedrive API evolution.*