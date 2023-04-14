# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" width="150" alt=""><figcaption></figcaption></figure>

Paloma is a fast, permissionless, Cosmos-SDK blockchain that  moves messages securely, between any other blockchains.

**Chain ID**: messenger | **Latest Version Tag**: v0.11.6 | **Wasm**: ON

[Website](https://www.palomachain.com) | [Discord](https://discord.gg/tKVFpfdSw4) | [Twitter](https://twitter.com/paloma_chain)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/paloma](https://explorer.kjnodes.com/paloma)

## Public endpoints

* api: [https://paloma.api.kjnodes.com](https://paloma.api.kjnodes.com)
* rpc: [https://paloma.rpc.kjnodes.com](https://paloma.rpc.kjnodes.com)
* grpc: paloma.grpc.kjnodes.com:10090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@paloma.rpc.kjnodes.com:10656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@paloma.rpc.kjnodes.com:10659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/paloma/addrbook.json > $HOME/.paloma/config/addrbook.json
```

**live-peers** (15)
```bash
peers="e833844c00b8ce60ce6826f170becfa18e6172c2@46.4.27.59:26656,7eae755c119f538e0dc99f3c37289de628bc9526@209.182.239.169:26656,99c890c97afc8abfdfeff662d539af5c504a0baf@88.99.67.234:26656,810bea15ec11d510dd33170851ee2ab74c48b6de@81.0.221.57:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,41a47bae18f81c1f626e4b238221b77e274424d7@45.33.65.223:26656,b92c94f00b46500a5ff8920acd438c0873c2f9da@50.116.13.101:26656,317141e329bc214a76ba92201f6818574ebe5323@135.181.114.98:36656,8ed8cddfac504d986a2c6545def0e57b2c6aa5db@65.109.106.172:38656,08c242d4505c5db223647069fdc0acb6e90079aa@65.109.106.214:26656,87b4221770495e66e772a53bbea92a15aff288c2@144.126.158.0:26656,98b54cd6696e616fe966008ebf2bac409e3e0773@65.108.194.44:26656,2c6772b11c1f9eff2a923eb2bf808543cdd501c5@79.143.179.196:26656,f4c43099e04b721c54a454dad85f61da49be90bc@65.108.199.222:28656,124cbe860f1eaa8084444587928db17c78ebd8f3@149.90.94.145:26658"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
