# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="7d1cc3e1d9c5f146528dde80dda9336ec703a1b3@65.109.135.114:18656,8a0e76b9cdfe2e80bca2e9ea270d57af17cfaf06@65.108.146.240:18656,5f1bcdfe67b0cd55ed12a06454206c7f1ab4b35b@95.216.160.203:26656,09e827239851ba5231bcaa47bbfbbc38d8289460@65.108.148.131:18656,4b1b5e4a8f3a0cbaf235b13e68184a2d9d376b2b@178.20.44.156:26656,42c4ff59e86b5473a7771deee48e8563af2a5ed3@195.2.80.130:26656,9119177769a7fd09447c0c9d819215c15440c6c9@77.120.115.146:15556,881418c296ee6744b7ac5ffa73441aa46ae0171b@155.133.27.235:26656,d0319b11dfc72aaaef562850ea19fb23224319c2@80.85.242.69:26656,3cc483fab14b58c807b583115376e2446f1c06e2@167.114.119.80:55656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
