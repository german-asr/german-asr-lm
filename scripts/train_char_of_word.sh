text_path=$1
output_path=$2

order=1
echo "Train order ${order}"
lmplz \
     --text $text_path \
     --arpa $output_path/lm_${order}.arpa \
     --o ${order} \
     --prune 0 \
     -S 80G \
     --discount_fallback

order=2
echo "Train order ${order}"
lmplz \
     --text $text_path \
     --arpa $output_path/lm_${order}.arpa \
     --o ${order} \
     --prune 0 0 \
     -S 80G \
     --discount_fallback

for order in 3 4 5 6; do
    echo "Train order ${order}"
    lmplz \
         --text $text_path \
         --arpa $output_path/lm_${order}.arpa \
         --o ${order} \
         --prune 0 0 0 \
         -S 80G \
         --discount_fallback
done
