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
peers="b57b9573b55c57c534cdb70a53138dec739b519d@212.23.222.220:26356,1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,7143126daf3c0983745a0b10b83c8e794c4fb2fc@65.108.126.46:33656,6ca675f9d949d5c9afc8849adf7b39bc7fccf74f@164.92.98.17:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,756368e62cbff16f8d0edcc4d169a090464bed53@38.242.194.233:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,7ac1bce20b8ea73bb301201f446f2e6ae06f7ff6@65.109.104.118:61056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
