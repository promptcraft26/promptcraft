# Detailed Human Evaluation Guidelines

## Evaluation Process Instructions

1. **Carefully read** the complete information of each test case
2. **Evaluate item by item** the scores for each dimension
3. **Fill in comments** explaining scoring rationale and improvement suggestions
4. **Ensure consistency** maintain the same scoring standards

## Technical Assessment Integration

**Technical correctness is integrated into effectiveness and overall quality scores:**
- Syntax errors, logical flaws, or incorrect assertions should lower effectiveness_score
- Technical implementation quality is reflected in overall_quality_score
- No separate technical_correctness field is needed

## Detailed Scoring Criteria Explanation

### Test case relevance to target contract

- **1 points**: Completely irrelevant - Case is completely unrelated to contract functionality or targets wrong contract
- **2 points**: Weakly relevant - Only covers minor functions or edge scenarios of the contract
- **3 points**: Moderately relevant - Covers basic contract functionality but not comprehensive
- **4 points**: Strongly relevant - Covers main contract functions and core logic
- **5 points**: Fully relevant - Perfectly covers core contract functions and critical scenarios

### Test case realism and practicality

- **1 points**: Completely unrealistic - Scenario would never occur in reality, parameter values completely unreasonable
- **2 points**: Somewhat unrealistic - Very low probability of occurrence, parameter settings are forced
- **3 points**: Moderately realistic - Possible but uncommon, parameter settings are basically reasonable
- **4 points**: Quite realistic - Likely to occur in practice, parameter settings are reasonable
- **5 points**: Highly realistic - Closely matches real deployment and interaction scenarios, parameter settings are precise

### Test case effectiveness in detecting vulnerabilities (including technical implementation)

**Evaluation Criteria**:
- **1 points**: Completely ineffective - Cannot detect any security issues OR has critical technical errors (syntax/logic issues)
- **2 points**: Very ineffective - Can only detect extremely obvious issues OR has major technical flaws
- **3 points**: Moderately effective - Can detect some security issues but coverage is incomplete, may have minor technical issues
- **4 points**: Quite effective - Can detect main security vulnerabilities, coverage is relatively comprehensive, technically sound
- **5 points**: Highly effective - Can precisely detect target vulnerabilities including edge cases and complex scenarios, technically excellent

**Technical Considerations**:
- **Syntax**: Are there any syntax errors in the test case?
- **Logic**: Is the test logic sound and reasonable?
- **Assertions**: Are the expected outcomes correctly asserted?
- **Parameters**: Are input parameters valid and appropriate?

### Comprehensive quality of test case (including all aspects)

**Evaluation Criteria**:
- **1 points**: Extremely poor quality - Multiple critical issues across all dimensions, technically flawed, basically unusable
- **2 points**: Poor quality - Has obvious defects in multiple dimensions, requires significant modifications
- **3 points**: Average quality - Basically usable but needs improvements in some areas
- **4 points**: Good quality - Performs well in all aspects, only needs minor adjustments
- **5 points**: Excellent quality - Excellent performance in all aspects, well-designed and implemented, can be used directly

**Comprehensive Considerations**:
- Balance between relevance, realism, and effectiveness
- Technical implementation quality and correctness
- Test case completeness and independence
- Clarity of documentation and comments

**Scoring Suggestions**:
- If any dimension is particularly poor, overall score should not exceed 3 points
- If test case has critical technical errors, overall score should be 1-2 points
- Excellent test cases should score 4-5 points across all dimensions

## Comments and Suggestions Guidelines

### comments Field
Fill in specific scoring rationale and test case strengths/weaknesses:
- **Technical Issues**: Note any syntax errors, logical flaws, or assertion problems
- **Strengths**: Aspects where test case design excels
- **Weaknesses**: Issues that need improvement
- **Scoring Rationale**: Why this score was given

### suggested_improvements Field
Provide specific improvement suggestions:
- **Technical Improvements**: Suggestions for syntax, logic, assertion corrections
- **Scenario Expansion**: Suggested additional test scenarios or edge cases
- **Documentation Improvements**: Suggestions for description and comment enhancements

## Frequently Asked Questions

**Q: How to handle test cases with technical errors?**
A: Score effectiveness_score and overall_quality_score lower, and describe the technical issues in comments.

**Q: What if a test case is technically perfect but targets the wrong functionality?**
A: Score relevance_score low, and note the issue in comments. Overall score should reflect this major flaw.

**Q: How to balance scores across different dimensions?**
A: Consider overall_quality_score as a summary that should reflect performance across all dimensions.
