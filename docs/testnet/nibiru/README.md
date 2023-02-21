# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-2 | **Latest Version Tag**: v0.16.3 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)




## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: [https://nibiru-testnet.grpc.kjnodes.com](https://nibiru-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (39)
```bash
peers="5eecfdf089428a5a8e52d05d18aae1ad8503d14c@65.108.141.109:19656,d2b6baed49aa475eb6ec5958bfbca30a61363b86@154.53.52.212:26657,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,5a868d18a5046b715ee726a45b680a68f92bafcb@149.102.136.149:27656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,438701ce016699880f9073c6b99f71d17309d820@154.53.52.215:26657,1edd1232fe59fd00a13bfdd9ac273e48b20f11c3@65.108.231.124:12656,0caedae543d21fe055dbabc195225b38a48951cd@173.249.0.229:26656,334af61b52388924e3a1c6ac1af57ffbac2ad752@84.46.255.14:26656,0d7d4f9b5dfe2dcc9c313fa3695eacd22e132a1b@125.111.119.12:26657,8ff8d3effc84c1e5d7bdff36d8921875f7436bcd@65.108.13.185:26858,a08e5b25443d038b08230177456ee23196509dd5@65.109.92.79:12656,24016cec78971d7ecae24fd99ac16655e6332eb8@66.94.102.176:26657,2e2a71b2fc86986a7940df724ce100c45cca3649@66.94.104.184:26657,cf29df0bc1d8a1d9053d7dc6bd7b8ee69b3021cc@51.89.47.31:26656,a71be69ab3cae88b9100cc357163e003b11291d1@155.133.22.116:26656,ff60133778ab80489636a81ec861b508e6d6aca4@34.168.169.45:26656,3faa0c05974e08e667281e62afcd781575c56b55@38.242.159.201:26656,ab5a794451f4b19055300f692160f4f20d55a891@82.208.21.81:26656,09de7d3f5acc5e421247a582aa50d601571415fb@38.242.202.200:26656,a94ef19317c0b592cc3d6ac10501d0f4fc099d47@85.173.113.198:21656,b502caa5e8071c14179c562a328bb2a096f6b44a@141.94.139.233:30656,e4ea6ffd9ec8ca5db91506e0429613628f0f61ee@155.133.22.115:26656,98032241ea61ca6ac066b8fa508baace6678a7a3@190.2.155.67:31656,e84bc060d4d4fe82ea2d7a181f28ddac62b1bb8a@65.109.131.71:26656,fa9913e5818acda6f0d06f3473a96052816fd51a@154.53.34.124:26657,a422bbf59756a9584ddc6f97a8b96bb15b596db7@34.73.61.37:26656,52dacee88cf2b6dc8f6e2c1876880bf370796e72@185.219.142.214:39656,10c9aecb4f414d45863cbe1a5f91d04b33fcb638@80.85.242.54:16656,e63604bb6323eaafb02a72cb825d770fd7f1998c@65.109.70.23:19856,2a11b3e06f832e430efb41e3c3bb07a42875d20c@154.53.34.112:26657,a575313137ddc0dae09fc79ad5558f2ca25867af@199.175.98.114:26656,627e39156fc505e60eb5e40402038218cf368a20@90.188.59.213:26656,06b87408d9b9b7a0b821c967bbfc2baaf4bac61a@38.242.204.136:26656,b1b38341e4d443e2b8d97368c734c1578e4f01cb@46.151.27.109:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
