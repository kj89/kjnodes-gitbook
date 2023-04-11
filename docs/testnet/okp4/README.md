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

**live-peers** (26)
```bash
peers="82bb185819e5cf2bb6a9896447672efca27f28cb@65.109.15.202:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,0521f5697fd89fc58bfbe0867525a9fe9efc12f4@65.109.154.182:38656,ead118d7cbe51cbabf5a77b69db7255512f41023@88.208.34.134:60656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,874373b78d2cd50e716aa464bf407581d9305655@94.250.201.130:27656,603828b0b21b150ece5aeee9d548a259d08348ec@65.108.224.156:26656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,14f8949ab0a276d2e55c8fa6255430881978a619@185.192.96.236:26656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.135.127:26656,6a66a38bdd5895ec6f1ce18b3430860a30e18e02@142.132.149.118:26656,1f4fa23210cc1d086a928a3c6de7c24f6c8f17ba@202.61.226.120:16656,643988550263605405a7968c38fd11653bf75cd0@38.242.252.104:26656,8527f34bd6e542304809386896997d12d80e5e0e@65.108.237.232:29656,8bccab4596e8bc162763bad6597d43523e6c32f8@104.194.8.68:26656,eef77b5ae1c37f3e5809ff928c329dde906be388@65.108.133.73:21656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,9392c27a9a561c31e7a920dc6f577d663c473ef8@154.12.225.88:26656,9928d19b7663a6fa639eb7c1ee239e671edcbdb2@5.9.147.22:26616,1e48c09a0f78070e90ed49b2e3d59f8fdc188e74@162.55.234.70:55156,fe8bd9375c43a7cc6ef27e62d56af341a62e67c9@95.217.202.49:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
