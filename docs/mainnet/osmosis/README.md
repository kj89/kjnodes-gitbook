# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:29090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:29656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:29659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="f1fe0a080d561d37a94bea6022cbc0972395a0f4@65.108.121.190:2000,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,bcef965764a0d6bc15f1476c18133d52d0ff14b6@149.202.72.166:26624,6acf893525c9c43dee575dc23fcab3aa1523ea87@74.118.136.232:26656,12910da249bcee4cdafbef938b10b51c94c0057e@5.9.142.165:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,f96947493f1edd08058afaeaef8f5830cc70b8f2@15.204.197.10:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,5696d9806c883beb725fb469d90039d921107b5b@116.202.209.186:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,75bae7b2af60155b6687ca3e5f92010d35cb0c12@54.164.100.216:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,88fa3de90d06422b409ce6beb2367b94b2a1759e@51.79.17.73:26656,d929af809b87632e83a3e01379792e085a0bdd88@38.242.232.248:26656,07db7d141686559045bfd4f39feff5ecf5f57f15@141.164.55.118:10001,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,da7994c3dc691b1f24aa3811a11d90c27683a307@66.206.15.130:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,95dbddda671081fb433871fa612ff5291242d93d@45.67.221.200:26656,ab3be1a8b463ac07d457dcce7af6b95cc7bae46b@46.4.79.183:26736,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,e0f3b604f1df9bf6590c4cc09fee1e28f46b0b39@65.109.28.226:15656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,79824a84c7bc35716839ac9c47dc05cceabf42c0@34.173.85.215:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
