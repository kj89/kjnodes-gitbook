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
peers="14f8949ab0a276d2e55c8fa6255430881978a619@185.192.96.236:26656,7ba5d3721d98efd479b2a3f3b4df6ebd5fd2f119@109.123.243.135:26656,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,ead118d7cbe51cbabf5a77b69db7255512f41023@88.208.34.134:60656,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,874373b78d2cd50e716aa464bf407581d9305655@94.250.201.130:27656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,6a66a38bdd5895ec6f1ce18b3430860a30e18e02@142.132.149.118:26656,eef77b5ae1c37f3e5809ff928c329dde906be388@65.108.133.73:21656,e755eb8016c2f6f5303b2f8d503d9126d235e80f@138.201.35.56:26656,fe8bd9375c43a7cc6ef27e62d56af341a62e67c9@95.217.202.49:30656,643988550263605405a7968c38fd11653bf75cd0@38.242.252.104:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.135.127:26656,8bccab4596e8bc162763bad6597d43523e6c32f8@104.194.8.68:26656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,603828b0b21b150ece5aeee9d548a259d08348ec@65.108.224.156:26656,8527f34bd6e542304809386896997d12d80e5e0e@65.108.237.232:29656,0448864ede56d3c96d7d3bb8ea9f546b70cc722e@51.159.149.68:26656,8633177b18f9031b84beb690293d20dce1d0c20e@121.78.247.252:35656,8028015d1c6828a0b734f3b108f0853b0e19305e@157.90.176.184:26656,2ca4e1bed94cfe9fad160e704ccbabf95f438dee@65.108.129.29:60656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,b5484e85a8802e0489234904d2b3a2d3c0c16e71@135.181.116.246:26106,9392c27a9a561c31e7a920dc6f577d663c473ef8@154.12.225.88:26656,25f585481845af42add73178a71169ec06f312df@65.108.9.164:20456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
