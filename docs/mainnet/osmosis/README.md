# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:12990

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:12956
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:12959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="bcef965764a0d6bc15f1476c18133d52d0ff14b6@149.202.72.166:26624,29ecd1a65ce2c244ca90a1d190b3b8e58eed1ada@51.81.106.237:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,e17c0a849eb239acd9f08ba396dec0db149b6ffc@185.255.131.77:26656,aa88cb583b8d932cadfcfd40de6594a64200da93@167.235.135.248:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,1a4706c2194cbc055adf4eb89a7b24493bcf33f8@15.235.9.22:26656,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,e4485f292ae0ed3c3998873cb25fa6eda4af4ea4@207.148.88.210:26656,e0f3b604f1df9bf6590c4cc09fee1e28f46b0b39@65.109.28.226:15656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,afdedf1dff1e0d1e06036dd28dfe1633ec4204b9@3.217.47.126:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,12910da249bcee4cdafbef938b10b51c94c0057e@5.9.142.165:26656,2ff9bc1740a721a9baeda01abee181997bb65568@142.132.140.20:26656,1990bfb9135023ca697bbb8a8d0defb6e4669478@211.219.19.74:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
