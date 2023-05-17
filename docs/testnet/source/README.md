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

**live-peers** (9)
```bash
peers="a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,08e5694cbc077e361cc2e9daa7f91aa67797c92e@65.109.85.170:34656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,a833e9d068c7f5f32f411662c0430196a88aee91@65.109.65.248:28656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,756368e62cbff16f8d0edcc4d169a090464bed53@38.242.194.233:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
