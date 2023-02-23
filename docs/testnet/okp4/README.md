# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

OKP4 is a revolutionary public blockchain protocol where communities are incentivized to  share data and services confidently. To maximize value from data, it needs to be processed  by complex algorithms and pooled with other datasets, to create valuable knowledge.

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v4.0.0 | **Wasm**: OFF

[Website](https://okp4.network) | [Discord](https://discord.gg/okp4) | [Twitter](https://twitter.com/OKP4_Protocol)




## Chain explorer
[https://explorer.kjnodes.com/okp4-testnet](https://explorer.kjnodes.com/okp4-testnet)

## Public endpoints

* api: [https://okp4-testnet.api.kjnodes.com](https://okp4-testnet.api.kjnodes.com)
* rpc: [https://okp4-testnet.rpc.kjnodes.com](https://okp4-testnet.rpc.kjnodes.com)
* grpc: [https://okp4-testnet.grpc.kjnodes.com](https://okp4-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@okp4-testnet.rpc.kjnodes.com:36656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@okp4-testnet.rpc.kjnodes.com:36659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/okp4-testnet/addrbook.json > $HOME/.okp4d/config/addrbook.json
```

**live-peers** (41)
```bash
peers="fff0a8c202befd9459ff93783a0e7756da305fe3@38.242.150.63:16656,540e0e9b33b2d87315fdf7089404671581d36e94@95.217.203.43:26656,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,269d246537499d05698c183497c4263e899036a4@65.108.9.164:35656,ead118d7cbe51cbabf5a77b69db7255512f41023@88.208.34.134:60656,8af258bbe73f4c66127a7b3e8b1ec23fde2950a6@65.108.192.123:19656,cf5e82486c4568c29a20719a68210523826ceb00@65.108.229.102:26651,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,ffbd1adeb58928c3f400fab23c84c3c73badd7fa@65.108.226.44:29656,82bb185819e5cf2bb6a9896447672efca27f28cb@65.109.15.202:26656,052e10ce23cce3249f61853e2ca6a63102b7bddb@5.161.97.198:26656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,bff8e08c4c89f148ba6459f0ca13800b09e575dc@195.154.107.51:26656,8028015d1c6828a0b734f3b108f0853b0e19305e@157.90.176.184:26656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,d1c1b729eff9afe7dfd371f190df6282c82ccfad@65.109.89.5:31656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,6a66a38bdd5895ec6f1ce18b3430860a30e18e02@142.132.149.118:26656,2c6b5af41689145abb85f95cb49131ae9e193142@217.13.223.167:61356,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.135.127:26656,473369a53bfa8a0ac4af5a191407b30bc82e83be@74.208.94.42:14656,f7fb0f3248e4aed14e89bc4967d48c66b72e6f62@135.181.147.169:26656,90481aeb2485505f8844a7347dac9abcf5f7acbe@5.75.190.38:26656,643988550263605405a7968c38fd11653bf75cd0@38.242.252.104:26656,e9255dd3341db6cadf73b4f151c97e0cd14f0efb@65.108.45.200:27464,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,eef77b5ae1c37f3e5809ff928c329dde906be388@65.108.133.73:21656,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,fe8bd9375c43a7cc6ef27e62d56af341a62e67c9@95.217.202.49:30656,170e60ecc237b7aab2b8e45e1b2fedba36fca8f1@54.65.151.96:26656,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46673,1f4fa23210cc1d086a928a3c6de7c24f6c8f17ba@202.61.226.120:16656,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,8527f34bd6e542304809386896997d12d80e5e0e@65.108.237.232:29656,d4305fcb7b20dc96481a6ae6ae84f281f3413a4e@65.109.37.58:13656,f7e481df45bfbe62ea0553f5f6da34eaf4f688c3@194.34.232.225:26656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
