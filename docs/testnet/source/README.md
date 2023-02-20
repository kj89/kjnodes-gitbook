# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/source.png" width="150" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: OFF

[Website](https://www.sourceprotocol.io/) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)




## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: [https://source-testnet.grpc.kjnodes.com](https://source-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:28656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:28659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (10)
```bash
peers="9260303a16969bbf4360b462d80ce12f77c4d3a1@43.131.35.28:26656,ddb472d197b8a732bb3f8878035603769aa4c85b@161.35.75.82:26656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,6ca675f9d949d5c9afc8849adf7b39bc7fccf74f@164.92.98.17:26656,63d1b126558468634137b5705ab90151b16932f8@65.108.151.6:26656,2c20351736d27e50952695801a4d77122ead307f@62.171.180.83:26656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
