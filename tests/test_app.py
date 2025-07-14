def test_summary():
    from transformers import pipeline
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    text = "DevOps automates the software lifecycle."
    result = summarizer(text, max_length=30, min_length=10, do_sample=False)[0]
    assert "summary_text" in result
