# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://www.sourceprotocol.io) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: source-testnet.grpc.kjnodes.com:12890

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:12856
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:12859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (11)
```bash
peers="42bb6ea45070248f5ea1d7c26db7665498a5b8c4@173.249.42.162:28656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,05dbcd1bb0563107c5eeb98a8da9d6cd9197bfcd@65.21.129.95:21756,08e5694cbc077e361cc2e9daa7f91aa67797c92e@65.109.85.170:34656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,1c29673dc1fb273bffc55808a6118a61a08df830@65.108.151.10:26656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
