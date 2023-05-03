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
peers="2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,da23ed57fc3d03b3864c309b589f2b5130a04a9f@65.109.111.204:28656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
