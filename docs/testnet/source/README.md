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
peers="4ede26dd5fbb87bd9dba462fe2c3c3e39e15c8f2@207.180.224.128:46656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,7143126daf3c0983745a0b10b83c8e794c4fb2fc@65.108.126.46:33656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,805c327443d9a2b425d16a402c23cb9cbfa36388@178.18.243.46:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,f2936d8f0ae99b9fa99d179f746faacc9c41a5c3@65.108.158.181:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
