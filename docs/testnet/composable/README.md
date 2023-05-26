# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-2 | **Latest Version Tag**: v2.3.3-testnet2fork | **Wasm**: OFF

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

**live-peers** (18)
```bash
peers="20f2608c9bc262df91d96027e1d5054ddee9c86c@142.132.209.236:22256,154ca7686d9e503736292778901b0ebcadfcaea6@88.99.3.158:22256,e6aa2a81f4b48b99d4d3f2ecd7739596af56d34d@148.113.143.196:26656,156d57dfe94634eaba1c30f9ec2ce5ccee8410e1@65.21.88.12:2000,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,f5fe55ea62334c68d08e6565794fe5c472936bf8@95.217.57.232:56656,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,fe82bb3e15e4cee715f47a9ccb925134b9131669@46.4.213.193:26656,8859e665f2eca25da78aaf4d2e541407885b08d8@5.78.72.11:26656,7521d65a4102259fa26816383fea2f8f21a3b1ea@65.109.116.21:11154,698a0903e3b181c5ac1bad343e62a1fccfe1d10a@89.58.16.33:15956,17ef33af803d45dff5eb164c655ea3aa4b4fa147@75.119.135.34:15656,2ca32b1aba0208008738ddefe44d5239bef2e894@95.217.144.107:22256,7fc16efbb3e56d81245a0828198d580b3f246f58@51.91.30.173:3000,872c8a78a17a24d6f44e1126c46ef52069c7bb18@65.109.80.150:2630,0ae432ac467abe0dab936175ce39b413fee1756c@65.109.155.238:31656,a7fdc284303bc4a8e62782e2e8f81008ea45a2b2@5.161.104.182:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:26976"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
