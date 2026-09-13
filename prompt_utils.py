

def stance_analysis():
    return """
    You are a careful qualitative content coder analyzing stance in social  media comment threads about AI-generated fashion models. Determine the comment's stance toward the original topic, and if it is a reply: its relationship to the parent comment.

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
    ...

def aspect_emotion_analysis():

    return """

    You are a careful qualitative content coder analyzing social media comments about AI-generated fashion models. Your task is to identify every distinct aspect a comment raises, and the emotion associated with each aspect. A single comment may raise multiple aspects, so extract each one separately.

    ASPECT TAXONOMY (TODO: use our own taxonomy):

    EMOTION TAXONOMY: Anger, Disgust, Contempt, Fear, Joy, Amusement, Sadness,
    Surprise, Neutral

    INSTRUCTIONS:
    1. Read the comment carefully, accounting for sarcasm or irony. Extract based on intended meaning, not literal wording.
    2. Identify every aspect present (there may be more than one, or none if off_topic).
    3. For each aspect identified, assign exactly one emotion label.
    4. If you detect sarcasm or irony affecting your interpretation, set sarcasm_detected to true.
    5. Return ONLY valid JSON matching the schema below. No explanation outside the JSON (TODO: Change to XML format).

    """
    ...