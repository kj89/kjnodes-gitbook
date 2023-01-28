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

**live-peers** (27)
```bash
peers="2067e672ef241d6364c10b43eec2abc26e36b607@31.187.74.3:26656,d256380b9344798396e8b1a9c6985f4553a2e0ca@38.242.219.209:26656,82ff5277d6385a2e9cab7048d8df5f6757d02a8f@43.154.33.200:26657,a575313137ddc0dae09fc79ad5558f2ca25867af@199.175.98.114:26656,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,5a868d18a5046b715ee726a45b680a68f92bafcb@149.102.136.149:27656,efb2dd9cf401c6c1a97fda94183d52c5000ae8e9@38.242.252.157:26656,eb65c95ea745d1cb5f66e2fda5d5e1029f4dc43d@5.161.43.109:26656,b2c162da315d2e57b1cf86b2f8a2769e3c30e479@43.154.185.150:26657,5eecfdf089428a5a8e52d05d18aae1ad8503d14c@65.108.141.109:19656,55773ecd03044a5126e68ea943338c6086cfbad3@43.134.174.55:26657,c1d90ca59915ee94cd615304bfac8ddb9bdf2e76@43.156.25.107:26657,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656,da7182e3934b51c099d8901101a5821472aa9d3b@38.242.214.165:26656,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,7bdcba29302c7b61d9de004d5b2164e7a8d33b2b@173.212.239.216:39656,1edd1232fe59fd00a13bfdd9ac273e48b20f11c3@65.108.231.124:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,8d390c237aba0bc42d7015a1fb366aea2ad66387@185.144.99.55:26656,f0df45ae127a4237e0234cd0623fe360332abe96@91.236.36.174:26656,438701ce016699880f9073c6b99f71d17309d820@154.53.52.215:26657,82dde0f3c283ca231849376696d08c39c3d458ce@173.82.203.187:26657,2c22d9b9f767522ddea193bd9f3c5b75f44a5558@173.82.207.117:26657,594149b5209a696b5e9e648786f0ea6df30e1a2b@65.108.6.45:60656,921f6c20fd0f09fda058452cc1a57a039a84b760@155.133.27.10:26656,8f00ba98b37036302db681a2572487d1b36d2d48@89.117.63.35:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
