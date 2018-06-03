how to use this program:
<ol>
    <li><h4>obtaining data:</h4>
        <ul>
            <li><h5>we obtain data using scikit-learn database "Labeled Faces in the Wild"</h5></li>
            <li><h5>we put images of yhe same size, that don't contain any faces in folder neg_ex(or slice one with bigger size)</li></h5>
        </ul>
    </li>
    <li><h4>train a Linear SVC model using given data<h4></li>
    <li><h4>finding "thing" on given photo</h4>
        <ul>
            <li><h5>slide frame over phot</h5></li>
            <li><h5>if model finds "thing" draw rectangle</h5></li>
        </ul>
    </li>
</ol>