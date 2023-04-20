# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

OKP4 is a revolutionary public blockchain protocol where communities are incentivized to  share data and services confidently. To maximize value from data, it needs to be processed  by complex algorithms and pooled with other datasets, to create valuable knowledge.

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v4.1.0 | **Wasm**: OFF

[Website](https://okp4.network) | [Discord](https://discord.gg/okp4) | [Twitter](https://twitter.com/OKP4_Protocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/okp4-testnet](https://explorer.kjnodes.com/okp4-testnet)

## Public endpoints

* api: [https://okp4-testnet.api.kjnodes.com](https://okp4-testnet.api.kjnodes.com)
* rpc: [https://okp4-testnet.rpc.kjnodes.com](https://okp4-testnet.rpc.kjnodes.com)
* grpc: okp4-testnet.grpc.kjnodes.com:36090

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

**live-peers** (30)
```bash
peers="30092d2717053f1c0813e8354c07c761c9c3ac5c@194.163.161.234:26656,23e895e7d650f43e1f53522165607b71685f8cfa@65.108.75.107:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,0521f5697fd89fc58bfbe0867525a9fe9efc12f4@65.109.154.182:38656,584871b6f75e970f5a95f9532fdc05fc91d6b447@65.109.116.204:20456,874373b78d2cd50e716aa464bf407581d9305655@94.250.201.130:27656,ead118d7cbe51cbabf5a77b69db7255512f41023@88.208.34.134:60656,c5616b6e6a0612f8800898e8e3ced17ffd87877a@51.178.65.184:26656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,14f8949ab0a276d2e55c8fa6255430881978a619@185.192.96.236:26656,78d923333e39e747c6a7fbfcc822ec6279990556@91.211.251.232:28656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,603828b0b21b150ece5aeee9d548a259d08348ec@65.108.224.156:26656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,8028015d1c6828a0b734f3b108f0853b0e19305e@157.90.176.184:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.135.127:26656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,d1c1b729eff9afe7dfd371f190df6282c82ccfad@65.109.89.5:31656,6a66a38bdd5895ec6f1ce18b3430860a30e18e02@142.132.149.118:26656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,1e48c09a0f78070e90ed49b2e3d59f8fdc188e74@162.55.234.70:55156,8bccab4596e8bc162763bad6597d43523e6c32f8@104.194.8.68:26656,0ef08b8e85a4803b75ed5d32f13e0b4f78afe855@65.109.80.158:13656,fe8bd9375c43a7cc6ef27e62d56af341a62e67c9@95.217.202.49:30656,9392c27a9a561c31e7a920dc6f577d663c473ef8@154.12.225.88:26656,c5ef62186e9aad1f83cab06f91533d1d5709bba7@65.109.117.212:13093,e755eb8016c2f6f5303b2f8d503d9126d235e80f@138.201.35.56:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
