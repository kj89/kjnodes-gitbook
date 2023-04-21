# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" width="150" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:55090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:55656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:55659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="ad417c4efa59e21b43e8e256c73b9939f1c22a0e@23.88.42.28:31656,f075e82ca89acfbbd8ef845c95bd3d50574904f5@159.69.110.238:36656,36ca8d32631eeb973322aec9b8a9b810d5344cd4@91.201.113.194:56656,3979193577e4e379c6f81b130807ed8c8d4b4d84@5.189.178.222:36656,001933f36a6ec7c45b3c4cef073d0372daa5344d@194.163.155.84:49656,1d61222b7b8e180aacebfd57fbd2d8ab95ebdc4c@65.109.93.152:35656,45d9fba9830260e6ee302ab3b3802f354aa3e5d8@65.109.69.240:36656,21ca2712116138429aed3d72422379397c53fa86@65.109.65.248:34656,6541f56cd9dc3fd6239354a8be74bc3f8841f995@5.161.77.184:15656,fadb0419474828f6f340978aeba7893cca42f25f@65.109.157.236:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
