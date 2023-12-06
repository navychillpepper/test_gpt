import streamlit as st
import openai

#챗지피티에게 글요약을 요청하는 함수
def askGPT(prompt,apiKey):
    client = openai.OpenAI(api_key=apiKey)
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages=[
            {'role':'user','content':prompt}
        ]
    )
    finalResponse = response.choices[0].message.content
    return finalResponse

## main 함수
def main():
    st.set_page_config(page_title='요약 프로그램')

    # session_state 초기화
    if 'OPENAI_API' not in st.session_state:
        st.session_state['OPENAI_API'] = ''

    with st.sidebar:
        openai_apiKey = st.text_input(label='OPEN API 키',placeholder='Enter your api key')

        if openai_apiKey:
            st.session_state['OPENAI_API'] = openai_apiKey
        st.markdown('----')

    st.header(':santa: 요약 프로그램 :christmas_tree:')
    st.markdown('----')

    text = st.text_area('요약할 글을 입력하세요.')
    if st.button('요약'):
        prompt = f'''
        **Instructions** :
    -You are an expert assistant that summarizes text into **Korean language**.
    -Your task is to summarize the **text** sentences in **Korean language**.
    -Your summarize should include the following :
        - Omit duplicate content, but increase the summary weight of duplicate content.
        - Summarize by emphasizing concepts and arguments rather than case evidence.
        - Summarize in 3 lines.
        - Use the format of a bullet point.
    -text : {text}
    '''
        st.info(askGPT(prompt,st.session_state['OPENAI_API']))

if __name__ == '__main__':     #### __main()__ 이 페이지 만들때 기계가 읽는 시작점이니까 꼭 넣어줘. 중요해 이거!
    main()