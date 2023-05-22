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
peers="05dbcd1bb0563107c5eeb98a8da9d6cd9197bfcd@65.21.129.95:21756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,c5eccf228a25f979592297311bfe2cc8ef94e482@95.111.229.159:26656,596112703a361a71e0c3dbf1b1b04f87e1c23e47@85.239.230.135:26656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,7ac1bce20b8ea73bb301201f446f2e6ae06f7ff6@65.109.104.118:61056,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656,c4a25dde02d45af2d9f90e10d136c5d399183730@38.242.137.186:28656,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
