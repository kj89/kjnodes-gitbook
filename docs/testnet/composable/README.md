# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-2 | **Latest Version Tag**: v2.3.2 | **Wasm**: ON

[Website](https://www.composable.finance) | [Discord](https://discord.gg/composable) | [Twitter](https://twitter.com/ComposableFin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/composable-testnet](https://explorer.kjnodes.com/composable-testnet)

## Public endpoints

* api: [https://composable-testnet.api.kjnodes.com](https://composable-testnet.api.kjnodes.com)
* rpc: [https://composable-testnet.rpc.kjnodes.com](https://composable-testnet.rpc.kjnodes.com)
* grpc: composable-testnet.grpc.kjnodes.com:15990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@composable-testnet.rpc.kjnodes.com:15956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@composable-testnet.rpc.kjnodes.com:15959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/composable-testnet/addrbook.json > $HOME/.banksy/config/addrbook.json
```

**live-peers** (21)
```bash
peers="bf95ad80f82320b8fefea75eeede60f563d1f847@168.119.91.22:26656,4ea491a39a329b2ef2d919b9e8cfdb3494bc5efe@65.109.23.237:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,3a12870f1084f5c3a95f0b2bf9a8070c2e52465b@94.16.117.238:22156,b672b0e847fd404866a9466baa59053709113222@185.188.249.46:15956,9ce5b6397c8f11a93242d619e0126a6164e42bc8@5.78.103.231:26656,c04a07a5feabf52ecdabe752a0a81bbb25402885@194.163.168.62:15956,2b8ba316083cf09ea7c316666454097e5bb0a4a8@116.202.227.117:15956,4c1ea1da9fb0442201e79535d71f66a5e0e1e68c@51.91.30.173:3000,20f2608c9bc262df91d96027e1d5054ddee9c86c@142.132.209.236:22256,514fff92cf4e97bb4357c361f87adbfcd47f56ad@65.109.117.208:26656,249d8915c9765eb0744bf8a26efc354fdb57ee21@46.4.5.45:22256,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:26976,c5ecf0c560b7d269dbcc184aca9636835a8c1597@195.3.220.22:12656,8553443b473e6e6a5d3403511d7c3be64904048d@85.239.234.199:26656,a39973a3ea8e5d9228c20e1c2a83f946fe1fb342@51.250.4.215:36656,c0fad6f415a8913ff63981586c4518ebcd615d69@128.140.57.144:26656,c97dd69796a3f55fb00d92358ec34a8185e28212@5.9.79.121:49656,9f111b0dd81a1dc39ad83f3cd2adc0b9948c7533@95.216.75.119:15956,e8f3c2f68733638574e78e85df6e8bcfef87d839@65.108.73.88:2340,7eabe041d60e63a88591a5c30ca890a9de36119c@3.133.131.224:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
