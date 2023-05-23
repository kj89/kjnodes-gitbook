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
peers="da23ed57fc3d03b3864c309b589f2b5130a04a9f@65.109.111.204:28656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,3e16844d041df0f4b14d0d624fc94eadf50ed61d@65.108.13.154:28656,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656,6ca675f9d949d5c9afc8849adf7b39bc7fccf74f@164.92.98.17:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,1709ae02a391357bad468987e208075ef53f969b@3.135.249.173:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
