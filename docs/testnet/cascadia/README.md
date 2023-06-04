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
peers="36b691f71f0bc07ec70fefdeedb14f876d484342@128.140.6.198:26656,a47973f2e731fc35ea0f1e2d115b51ee77b91827@109.123.249.188:26656,417e5565608968e10c88be36b13fcb03e00e48ee@95.217.199.48:26656,6e8c7e7e12c03843eb4090a8d8f26bcee487da37@194.163.134.39:26656,3ae7f63ee1cf8ea10a4596c4d5d46bb2074500fb@65.109.99.123:26656,f2a5f1a90fd0b9f9cf85223ddc78a4b936f26d5d@95.217.72.99:39656,09e827239851ba5231bcaa47bbfbbc38d8289460@65.108.148.131:18656,e80bb40ed1d6f509c21c1627ba4c14d838c71550@144.126.154.230:55656,4ec51eeff609e98100beb77bfb34fec9add6057d@45.14.194.130:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,d3e1ce95ac1e2830296eff1c952b89d6c3d84f7a@217.197.117.53:61256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
