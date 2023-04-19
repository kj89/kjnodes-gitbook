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

**live-peers** (10)
```bash
peers="2a7eae11dc3af3d70b295e6d1e61412a4ffb8d97@136.243.103.32:26656,45d9fba9830260e6ee302ab3b3802f354aa3e5d8@65.109.69.240:36656,3979193577e4e379c6f81b130807ed8c8d4b4d84@5.189.178.222:36656,001933f36a6ec7c45b3c4cef073d0372daa5344d@194.163.155.84:49656,d5ba7a2288ed176ae2e73d9ae3c0edffec3caed5@65.21.134.202:16756,5623331ab53459146cbb60efadf42899373f844b@37.27.6.70:26656,8757ec250851234487f04466adacd3b1d37375f2@65.108.206.118:61556,e25bf22448e62faca2359985303ec4557f662444@95.217.11.20:26656,3d95bfa6a3af10c782a70f1c93d87203acd252eb@65.109.111.159:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
