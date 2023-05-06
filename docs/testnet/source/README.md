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
peers="1609741985ae89ab709311ed6b898f79c7ec0322@206.189.54.116:26656,42bb6ea45070248f5ea1d7c26db7665498a5b8c4@173.249.42.162:28656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,291a397d001fca8cf2991dfce8bc6f724d44295c@75.119.132.25:29656,da23ed57fc3d03b3864c309b589f2b5130a04a9f@65.109.111.204:28656,c4a25dde02d45af2d9f90e10d136c5d399183730@38.242.137.186:28656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656,49b025c08193c8846956423ac80504b0bab2b777@185.182.187.239:26656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
