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

**live-peers** (29)
```bash
peers="1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,5696d9806c883beb725fb469d90039d921107b5b@116.202.209.186:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,d557fd150f11883e93c23d8fcab19ef343db8096@35.215.38.241:26656,8e72d0b37a9dc16ea58c0da705caa6530badd6ce@138.197.68.193:26656,fae5ea7e5e08795fa404265d2b2d78b417a06d79@23.108.108.110:26657,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,c29b58aa25198ef724189f9a0b8d7ef4399d9587@65.109.52.178:26656,4d2605490fcd7369800cb0e1e27ef6d433c1cd96@65.109.20.37:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,a559df67d051d54627a3e25584ff18b8ca55a8b0@95.216.46.251:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,1a4706c2194cbc055adf4eb89a7b24493bcf33f8@15.235.9.22:26656,d40d9763093fa618ce3adbdd0e6758a5b33e9ca4@173.215.85.171:20050,3243426ab56b67f794fa60a79cc7f11bc7aa752d@35.210.252.64:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,4c927f93d430baf31e6d6418e62c56f442f092bc@46.4.28.42:26656,2186d344ff775c8181bf31de600eed0c72b9fe9e@65.109.28.213:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,92551df875dc01b752d3560aee5ffe0007841a60@50.230.104.196:26656,bfcbd83f2ecfc2e839b246a001e355079e66f0fd@24.199.110.108:30799,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,8908c0a7e370708a26269a39fecc46d41bdbc26d@65.108.230.113:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
