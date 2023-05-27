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
peers="9410da5f763b47341b3b85f510d4260e47f0ed97@5.189.144.237:18656,af8b5486e4938c3bd9ab56fd5ee03d26857089a1@31.220.95.213:26656,c0dc36f56816b90889d8f0702adcf265f6fc022a@65.108.251.82:18656,035df68157b66066b00390d74c6d4f4895cb1ef9@95.217.155.184:26656,783a3f911d98ad2eee043721a2cf47a253f58ea1@65.108.108.52:33656,794f20c290e46840479a51f760e67adbfb6915e2@65.109.137.4:18656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,bc62371aa967cf2ecac4d045393a80ad92ec76f8@109.123.255.8:18656,a47973f2e731fc35ea0f1e2d115b51ee77b91827@109.123.249.188:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
