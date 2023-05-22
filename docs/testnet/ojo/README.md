# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: ojo-testnet.grpc.kjnodes.com:15090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:15056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:15059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (10)
```bash
peers="2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,2905d22a658a7138c03c0259fba4c168260682bb@159.69.208.78:26656,1626881c604cba71cbbc8cddd0fb5a5cb2adf2f0@87.106.114.73:33656,5af3d50dcc231884f3d3da3e3caecb0deef1dc5b@142.132.134.112:25356,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,1786d7d18b39d5824cae23e8085c87883ed661e6@65.109.147.57:36656,a1a6edee9e7928c97d8f99805757c09a1248b942@194.195.87.28:34656,eb329e1907bc9a519e863824e57cf5222cf45ec9@143.198.145.207:28656,5a53ebe6e029f8a26b1bc6dd8fe9a8efd57202f6@167.71.194.75:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
