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
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,c2f8425fdc5907f9b5834ac66e634d2ae03cdc71@185.52.52.30:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,aa88cb583b8d932cadfcfd40de6594a64200da93@167.235.135.248:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,59655a4db8843a411f9bcb8b5b2105998f1e340b@176.103.222.159:26656,2904827f3ffa642bf7122d65cef27e1ab40a7346@35.74.104.174:16656,e6b9d01d5adc8ab1106f142b18f5ea5da00ec306@144.76.82.52:26656,b8337f4d5f8872b094c5df513b49d9d795a57e3e@220.130.223.158:27756,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,50d2c6d6ef06cec7167cb2588636ae3593f575a5@86.111.48.150:26656,1990bfb9135023ca697bbb8a8d0defb6e4669478@211.219.19.74:26656,1a4706c2194cbc055adf4eb89a7b24493bcf33f8@15.235.9.22:26656,5696d9806c883beb725fb469d90039d921107b5b@116.202.209.186:26656,e0f3b604f1df9bf6590c4cc09fee1e28f46b0b39@65.109.28.226:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
