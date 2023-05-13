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
peers="7a288e8d085b5aad8d43b0c6e6dbb8498588c206@5.182.17.164:26656,b57b9573b55c57c534cdb70a53138dec739b519d@212.23.222.220:26356,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656,67958f716999fdc47fac777f0605a1911653ae86@65.109.48.181:30656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,da23ed57fc3d03b3864c309b589f2b5130a04a9f@65.109.111.204:28656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
