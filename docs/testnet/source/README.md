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

**live-peers** (10)
```bash
peers="7a288e8d085b5aad8d43b0c6e6dbb8498588c206@5.182.17.164:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,b57b9573b55c57c534cdb70a53138dec739b519d@212.23.222.220:26356,1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,291a397d001fca8cf2991dfce8bc6f724d44295c@75.119.132.25:29656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,596112703a361a71e0c3dbf1b1b04f87e1c23e47@85.239.230.135:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
