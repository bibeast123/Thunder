""" Contains summarizing function"""

from summarizer import Summarizer

def create_summary(transcript_path, summary_path):
    """Creates a summary of the trascript using the path of the transcript

    Args:
        transcript_path (str): transcript path
        summary_path (str): summary path

    Returns:
        str: summary
    """

    with open(transcript_path, "r") as f:
        text = f.read()
    
    text.replace('{}', '')
    model = Summarizer()
    s = model(text, num_sentences=4)

    with open(summary_path, "w") as f:
        f.write(s)
    
    return s


