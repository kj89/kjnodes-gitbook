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
peers="4ead67f38f3163a5c849333faaaf760b6d9eda8e@185.237.253.88:26656,881418c296ee6744b7ac5ffa73441aa46ae0171b@155.133.27.235:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,c6e3921222655345d8296353994e917f13a1b4a1@65.109.92.79:40656,cc42f2077c770816514e0e4d3076189d743752a2@65.109.163.85:26656,7d1cc3e1d9c5f146528dde80dda9336ec703a1b3@65.109.135.114:18656,1ca21c62b676383e9f4dcc263f29098ed9916995@185.193.67.105:26656,345f933bde192fdbab6493aa814345618d8ad6d9@194.163.150.104:26656,e6e3fbc13c1903ac758ce7c6fa180312b89af2e8@142.132.248.253:25656,5e75648d2e0cee67e5b3908546163f2ef7b16109@5.78.66.127:18656,d3e1ce95ac1e2830296eff1c952b89d6c3d84f7a@217.197.117.53:61256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
