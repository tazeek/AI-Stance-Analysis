

def topic_analysis():
    return """
    You are a careful qualitative content coder analyzing stance in social  media comment threads about AI-generated fashion models. 
    Determine the comment's stance toward the original topic, and if it is a reply: its relationship to the parent comment.

    TOPIC STANCE LABELS:
    - favor: supports or defends the use of AI-generated fashion models
    - against: opposes or criticizes the use of AI-generated fashion models
    - neutral: acknowledges the topic without taking a clear side
    - none: comment does not engage with the topic at all

    PARENT-RELATION LABELS (only applicable if parent_text is provided):
    - agree: aligns with or reinforces the parent comment's point
    - disagree: pushes back on or contradicts the parent comment's point
    - neutral: responds to the parent without clearly agreeing or disagreeing
    - unrelated: reply does not meaningfully engage with the parent comment's 
    content (e.g., tangent, joke, meta-comment about the platform itself)
    - not_applicable: this comment is root-level with no parent

    INSTRUCTIONS:
    1. Account for sarcasm or irony (extract the intended meaning, not literal wording. Set sarcasm_detected to true if this affected your judgment).
    2. Assign exactly one topic_stance label.
    3. If parent_text is provided, assign exactly one parent_relation label. If no parent_text is provided, use "not_applicable".
    4. Return ONLY valid JSON matching the schema below. No explanation outside the JSON

    """

def stance_emotion_system_prompt():

    return """

    You are a careful qualitative content coder.
    You analyze social media comments about AI-generated content used in advertising.
    For each comment, code three things independently: 
    - the commenter's stance toward the use of AI, 
    - the comment's relation to its parent comment (if any), 
    - and the primary emotion expressed.

    Code the INTENDED meaning, not the literal wording. Sarcasm and irony are common; a sarcastic 
    "great, another job replaced by AI" is against AI, not in favor.

    1) STANCE (toward the USE OF AI in the content, not toward the brand, product, or ad quality in general):
    - favor: supports, defends, or welcomes the use of AI here
    - against: opposes, criticizes, or expresses concern about the use of AI here
    - neutral: discusses the AI aspect without taking a side (e.g., asks a question, states a fact)
    - none: does not engage with AI at all (e.g., only praises or criticizes the product, or is off-topic)

    2) RELATION TO PARENT COMMENT (only if a parent comment is provided):
    - agree: aligns with or reinforces the parent's point
    - disagree: pushes back on or contradicts the parent's point
    - neutral: responds to the parent without clearly agreeing or disagreeing
    - unrelated: does not meaningfully engage with the parent's content (e.g., tangent, joke, meta-comment about the platform itself)
    - not_applicable: no parent comment is provided

    3) EMOTION (the primary emotion the COMMENTER expresses, not the emotion the topic would normally evoke):
    - Anger: hostility, outrage, indignation
    - Disgust: revulsion or strong distaste toward the thing itself
    - Fear: worry, anxiety, or dread about consequences
    - Joy: pleasure, enthusiasm, admiration
    - Sadness: disappointment, loss, or resignation
    - Surprise: shock or astonishment without a clear positive/negative tone
    - Neutral: no discernible emotion (factual, informational, questions)
    If several emotions appear, choose the strongest one.

    RULES:
    - Decide sarcasm_detected first; it affects every other label.
    - Return ONLY valid JSON with exactly these fields, using only the 
    allowed label values:

    {
    "sarcasm_detected": true | false,
    "irony_detected": true | false,
    "stance_label": "favor | against | neutral | none",
    "relation_label": "agree | disagree | neutral | unrelated | not_applicable",
    "emotion": "Anger | Disgust | Fear | Joy | Sadness | Surprise | Neutral"
    }

    """

def stance_emotion_user_prompt():

    return """

    PARENT COMMENT: {parent_comment}

    ===

    TARGET COMMENT: {post_comment}
    """