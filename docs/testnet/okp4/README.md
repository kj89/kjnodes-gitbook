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

**live-peers** (40)
```bash
peers="ffbd1adeb58928c3f400fab23c84c3c73badd7fa@65.108.226.44:29656,e20b9048c220d4a8b7e7934fddb3c4fb20c20bdd@81.0.246.196:26656,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,269d246537499d05698c183497c4263e899036a4@65.108.9.164:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,d7d3e978951ccf946f0e33805778c1961ad42819@31.7.196.21:26656,ead118d7cbe51cbabf5a77b69db7255512f41023@88.208.34.134:60656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,9392c27a9a561c31e7a920dc6f577d663c473ef8@154.12.225.88:26656,fff0a8c202befd9459ff93783a0e7756da305fe3@38.242.150.63:16656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,874373b78d2cd50e716aa464bf407581d9305655@94.250.201.130:27656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,c8771124d781b73a9184b8a3237f72837f167edd@5.75.205.215:26656,d1c1b729eff9afe7dfd371f190df6282c82ccfad@65.109.89.5:31656,fe8bd9375c43a7cc6ef27e62d56af341a62e67c9@95.217.202.49:30656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,e755eb8016c2f6f5303b2f8d503d9126d235e80f@138.201.35.56:26656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,8527f34bd6e542304809386896997d12d80e5e0e@65.108.237.232:29656,2c6b5af41689145abb85f95cb49131ae9e193142@217.13.223.167:61356,473369a53bfa8a0ac4af5a191407b30bc82e83be@74.208.94.42:14656,8af258bbe73f4c66127a7b3e8b1ec23fde2950a6@65.108.192.123:19656,ae5be91a24a5a454dd7d51b7762666d6ddc795ee@185.144.99.18:26656,e9255dd3341db6cadf73b4f151c97e0cd14f0efb@65.108.45.200:27464,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,eef77b5ae1c37f3e5809ff928c329dde906be388@65.108.133.73:21656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,90481aeb2485505f8844a7347dac9abcf5f7acbe@5.75.190.38:26656,0928743859aae996c2236bc376dbc168a22c5925@5.189.159.198:26656,5a460ead06c5fc1d6d70a1f858d874bf53463a4a@149.102.143.145:31656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26996,6a66a38bdd5895ec6f1ce18b3430860a30e18e02@142.132.149.118:26656,d132ad0c5b2afd0eab2d87351eeda46dc9d69312@46.228.205.200:26656,c6abcdff7b29159bf5be14f43c8e877648136468@51.159.2.19:23098,ef7c45199eb3cd79cbf7e906dcfa2c7de11e1499@167.235.15.19:32656,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46673"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
