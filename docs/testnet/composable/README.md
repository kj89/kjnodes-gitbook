# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-1 | **Latest Version Tag**: v2.2.0 | **Wasm**: ON

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

**live-peers** (30)
```bash
peers="bf95ad80f82320b8fefea75eeede60f563d1f847@168.119.91.22:26656,13c29d1d66d604e8920ba0170276368e4e77f249@88.99.3.158:22256,2b8ba316083cf09ea7c316666454097e5bb0a4a8@116.202.227.117:15956,c0fad6f415a8913ff63981586c4518ebcd615d69@128.140.57.144:26656,4775d0152d784b3ddf4f48c2d0ebddf961b52655@43.157.56.21:26656,4ea491a39a329b2ef2d919b9e8cfdb3494bc5efe@65.109.23.237:27656,4e073bf4729ba557e7726ad8acbc1d1b186e13de@134.209.38.116:26656,7ab89f884656a66ca90fd9d44489da3c6ca1fea4@95.217.144.107:22256,8553443b473e6e6a5d3403511d7c3be64904048d@85.239.234.199:26656,20f2608c9bc262df91d96027e1d5054ddee9c86c@142.132.209.236:22256,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,3a12870f1084f5c3a95f0b2bf9a8070c2e52465b@94.16.117.238:22156,7bff2e43489a7acd09a38ab47c1f25ec24e24947@51.79.101.169:26656,b672b0e847fd404866a9466baa59053709113222@185.188.249.46:15956,7eabe041d60e63a88591a5c30ca890a9de36119c@3.133.131.224:26656,b960daa0d03d18091906c50dd1312eaa62ca3ce4@136.243.88.91:2530,067f0f6f1706c4ef7da49b2896f28e194e8be055@96.234.160.22:30456,4870510889335804c39bab7fc5fa356eb94af74e@135.181.180.230:46656,4c1ea1da9fb0442201e79535d71f66a5e0e1e68c@51.91.30.173:3000,249d8915c9765eb0744bf8a26efc354fdb57ee21@46.4.5.45:22256,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:26976,f159e46072dcd5f78c2d64417200ca1dfb27636c@65.108.78.101:15956,a39973a3ea8e5d9228c20e1c2a83f946fe1fb342@51.250.4.215:36656,3c091edbe051f9b0e1bcf46200db163e667a114a@65.108.129.94:26656,760ae7ab2249b807e18b6d97a80976ac8839ec95@65.21.88.12:26656,c04a07a5feabf52ecdabe752a0a81bbb25402885@194.163.168.62:15956,c97dd69796a3f55fb00d92358ec34a8185e28212@5.9.79.121:49656,f23a8daca1f65aeee7ce6f6d47a56542a08538c9@66.45.233.110:26656,631feee431f86b0ad92d1c4a6a259b20e211e2ad@71.236.119.108:41656,d850d1525f38622c2e8ea97a2ff91c63f8c8669c@193.26.159.34:12656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
