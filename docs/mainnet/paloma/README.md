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

**live-peers** (16)
```bash
peers="98b54cd6696e616fe966008ebf2bac409e3e0773@65.108.194.44:26656,87b4221770495e66e772a53bbea92a15aff288c2@144.126.158.0:26656,dfa0d66a3713bf6b49bc509a2a4fc75bee042a30@23.88.77.188:20009,19165f3248f358ded53c3f51cf97a22123560b86@65.109.69.154:38656,527200c42834243b6dc8dacbe26423b7e6577e0f@138.201.129.102:26656,41a47bae18f81c1f626e4b238221b77e274424d7@45.33.65.223:26656,124cbe860f1eaa8084444587928db17c78ebd8f3@149.90.94.145:26658,8ed8cddfac504d986a2c6545def0e57b2c6aa5db@65.109.106.172:38656,5321570794c61a8285505812cb7ebd6308a86583@65.109.113.253:26656,b92c94f00b46500a5ff8920acd438c0873c2f9da@50.116.13.101:26656,16f0d09580054101394ea08bbb48b1ad5bb91a27@95.214.52.144:10656,31177b544fcf1cae76e3560812f4f901cab27126@65.109.61.175:26656,08c242d4505c5db223647069fdc0acb6e90079aa@65.109.106.214:26656,f4c43099e04b721c54a454dad85f61da49be90bc@65.108.199.222:28656,e4b7cdd48c39c355e9a3480f4f4d5afab8fb0e08@46.0.203.78:26637,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
