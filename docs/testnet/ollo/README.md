# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

Website: [https://www.ollostation.zone](https://www.ollostation.zone)


## Public endpoints

* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (34)
```
peers="b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656,ef8863e006ba8eaea3aa8b780b01b82b401d7bd9@84.46.252.45:56656,ed38d885d068a963b0bc3986bb69680c34757a40@135.181.83.157:26656,b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,1cb68888ccf57fc37edd40908b5e8ea810c3a64d@84.46.246.109:15656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,9c538c7faa0881052ff1cb21c031372ab510e064@209.126.12.135:26656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,4df1895f1e1d76bc317ca2698a3fea6354eadd77@65.108.15.48:26656,3baa3ab28418101d74a75e859b7ac0777f671c1c@65.108.204.119:26116,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,c5ffaa34423e83bf2d63c8780ead6977a19fa64e@65.109.30.117:36656,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,4b73754c2c10d523ffd43ca95d9cb6e0ad8204a4@5.189.148.147:26656,958c8c3198edc57b70dd3206eb15d20e1da92bb8@185.197.195.242:36656,70ba32724461c7ed4ec8d6ddc8b5e0b1cfb9e237@54.219.57.63:26656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,46d6f338d845f2eabf046d8bbabdab70a7d94b18@89.179.33.100:26656,83c109aacea2db21f46f9c4c5dbb5a7cbc81e6e1@178.62.62.90:26656,4da239f27366a2f0076163fc577afdc67d470a82@65.109.90.33:18156,0bee9e500e51465917506b47691a8fb032100da9@94.130.200.168:32656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,78d22e5ea3c135e0b9b8547c4b9da5333f124217@84.46.246.104:32656,ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
