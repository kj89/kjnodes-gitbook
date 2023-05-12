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

**live-peers** (10)
```bash
peers="76ecf5bcd797fb7335c8ec45236c137ebcf6bfc4@144.91.103.115:36656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,7a9cd31ca48252a741ef0689bc35b751bffd555c@89.117.49.164:26656,fcac681e16636bc1185194e31d0ff9b27d7f1275@85.239.233.241:55656,32bcc51674dd83a316323a67918c1cee25163291@65.109.72.12:26656,23c3d082bd3a3102988c04085531461daa5a4b21@65.108.81.122:26656,3abb2442a0c8822289c30f7715c3fb428269dbb5@95.216.246.139:656,d417eb06db1da1790b2a9238630731ec6ca9eeb5@91.142.72.79:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,c55cdbfbc70551cb877de8d72976422d1a525fda@173.249.38.240:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
