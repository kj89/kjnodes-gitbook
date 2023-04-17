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
peers="9f2df25f380a7e67a92c3dc5e7c33c08555b30dc@5.9.108.19:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,729219c108c059824ea9a17c09d11adc99226db4@66.172.36.139:36656,12910da249bcee4cdafbef938b10b51c94c0057e@5.9.142.165:26656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,3243426ab56b67f794fa60a79cc7f11bc7aa752d@35.210.252.64:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,5bda7b3070d62b4ddbea815e8bea6c6e9548d17d@65.108.140.115:26656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656,a6d449c9a3dd36ec99e46b2820dcb1bd50d6d956@135.181.62.108:26666,07db7d141686559045bfd4f39feff5ecf5f57f15@141.164.55.118:10001,5696d9806c883beb725fb469d90039d921107b5b@116.202.209.186:26656,f96947493f1edd08058afaeaef8f5830cc70b8f2@15.204.197.10:26656,79824a84c7bc35716839ac9c47dc05cceabf42c0@34.173.85.215:26656,236a60841401f53c28f7609ea50ea88feb259a1e@5.9.100.51:36656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
